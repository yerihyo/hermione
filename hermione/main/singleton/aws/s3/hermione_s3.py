from functools import lru_cache

import boto3

from foxylib.tools.function.function_tool import FunctionTool
from hermione.main.singleton.env.hermione_env import HermioneEnv


class HermioneS3:
    @classmethod
    @FunctionTool.wrapper2wraps_applied(lru_cache(maxsize=2))
    def client(cls):
        aws_access_key_id = HermioneEnv.env_key2value(HermioneEnv.Value.LOCAL, 'AWS_ACCESS_KEY_ID')
        aws_secret_access_key = HermioneEnv.env_key2value(HermioneEnv.Value.LOCAL, 'AWS_SECRET_ACCESS_KEY')
        resource = boto3.client('s3',
                                  aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key,
                                  )
        return resource

    @classmethod
    @FunctionTool.wrapper2wraps_applied(lru_cache(maxsize=2))
    def resource(cls):
        aws_access_key_id = HermioneEnv.env_key2value(HermioneEnv.Value.LOCAL, 'AWS_ACCESS_KEY_ID')
        aws_secret_access_key = HermioneEnv.env_key2value(HermioneEnv.Value.LOCAL, 'AWS_SECRET_ACCESS_KEY')
        resource = boto3.resource('s3',
                                     aws_access_key_id=aws_access_key_id,
                                     aws_secret_access_key=aws_secret_access_key,
                                     )
        return resource
