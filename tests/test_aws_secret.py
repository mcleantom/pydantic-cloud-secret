import pydanitc_cloud_secret
import unittest


class TestAwsSecret(unittest.TestCase):

    def test_aws_secret(self):
        pydanitc_cloud_secret.aws.get_secret("pydantic_cloud_secret/api-key", "eu-north-1")


if __name__ == '__main__':
    unittest.main()
