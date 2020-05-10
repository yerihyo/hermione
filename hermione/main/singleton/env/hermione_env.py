import os
import sys

import yaml
from pathlib import Path

from functools import lru_cache, reduce
from yaml import BaseLoader

from foxylib.tools.file.file_tool import FileTool
from foxylib.tools.function.function_tool import FunctionTool
from foxylib.tools.jinja2.jinja2_tool import Jinja2Renderer
from foxylib.tools.native.native_tool import BooleanTool
from foxylib.tools.string.string_tool import str2lower

from foxylib.tools.env.env_tool import EnvTool
from hermione.main.singleton.jinja2.hermione_jinja2 import HermioneJinja2

FILE_PATH = os.path.realpath(__file__)
FILE_DIR = os.path.dirname(FILE_PATH)
REPO_DIR = reduce(lambda x,f:f(x), [os.path.dirname]*4, FILE_DIR)


class HermioneEnv:
    class Key:
        SKIP_WARMUP = "SKIP_WARMUP"
    K = Key

    class Value:
        LOCAL = "local"
        DEV = "dev"
        STAGING = "staging"
        PROD = "prod"

        @classmethod
        def list(cls):
            return [cls.LOCAL, cls.DEV, cls.PROD]

    @classmethod
    def env(cls):
        return cls.env2norm(EnvTool.env_raw()) or "local"

    @classmethod
    def env2norm(cls, env):
        _env = str2lower(env)

        if _env in {"prod", "production", }:
            return cls.Value.PROD

        if _env in {"staging", }:
            return cls.Value.STAGING

        if _env in {"dev", "develop", "development", }:
            return cls.Value.DEV

        if _env in {"local", }:
            return cls.Value.LOCAL

        return _env

    @classmethod
    def is_skip_warmup(cls):
        nb = cls.key2nullboolean(cls.Key.SKIP_WARMUP)
        if nb is True:
            return True

        if nb is False:
            return True

        # raise Exception({"cls.env()":cls.env()})
        # return cls.env() in {cls.Value.LOCAL, cls.Value.DEV}
        return cls.env() in {cls.Value.LOCAL, }

    @classmethod
    @FunctionTool.wrapper2wraps_applied(lru_cache(maxsize=2))
    def _json_yaml(cls,):
        filepath = os.path.join(REPO_DIR, "hermione", "env", "yaml", "env.part.yaml")
        if not os.path.exists(filepath):
            return None

        data = {"HOME_DIR": str(Path.home()),
                "REPO_DIR": REPO_DIR,
                "ENV_DIR": os.path.join(REPO_DIR, "hermione", "env"),
                }
        utf8 = HermioneJinja2.textfile2text(filepath, data)
        json_yaml = yaml.load(utf8, Loader=BaseLoader)
        return json_yaml

    @classmethod
    def _env2target_envs(cls, env):
        __DEFAULT__ = "__DEFAULT__"
        env_norm = cls.env2norm(env)

        if env_norm in {cls.Value.DEV, cls.Value.STAGING, cls.Value.PROD}:
            return [env, __DEFAULT__]

        if env_norm in {cls.Value.LOCAL}:
            return [env, cls.Value.DEV, __DEFAULT__]

        raise NotImplementedError({"env": env})

    @classmethod
    def env_key2value(cls, env, k):
        # return os.environ.get(k)

        json_yaml = cls._json_yaml()
        envs = cls._env2target_envs(env)
        return EnvTool.json_envs_key2value(json_yaml, envs, k)

    @classmethod
    def env2dict(cls, env):
        return {key: cls.env_key2value(env, key) for key in cls.keys()}

    @classmethod
    def keys(cls):
        return list(cls._json_yaml().keys())

    @classmethod
    def key2value(cls, key):
        return cls.env_key2value(cls.env(), key)

    @classmethod
    def key2nullboolean(cls, key):
        v = cls.key2value(key)
        nb = BooleanTool.parse2nullboolean(v)
        return nb

