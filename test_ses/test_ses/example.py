#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""SESを用いたメール送信
"""

__author__ = "Taku Ikegami"
__version__ = "1.0.1"
__date__ = "2022/11/12(Created: 2022/11/12)"


import os

import yaml
from botocore.exceptions import ClientError
from boto3.session import Session
from jinja2 import Environment, FileSystemLoader


def read_yaml(*args):
    """yaml形式のファイルを読み込む

    Parameters
    ----------
    *args: tuple
    実行ファイルの場所を元にyamlのファイルを指定（ディレクトリの階層順にしていして最後にファイル名を指定する）

    Returns
    -------
    dict:
        yamlの設定ファイルを辞書形式で返す
    """
    with open(
        os.path.join(os.getcwd(), *args), "r", encoding="utf-8"
    ) as yaml_file:
        return yaml.safe_load(yaml_file)


def read_template(template_file, **kwargs):
    """メールの本文をテンプレートから読み込みレンダリングを行う

    Parameters
    ----------
    template_file:
        本文のテンプレートファイル名
    **kwargs : dict, optional
        テンプレートに埋め込むパラメータ
    """
    return (
        Environment(loader=FileSystemLoader("./", encoding="utf8"))
        .get_template(template_file)
        .render(kwargs)
    )


def send_mail():
    """メール送信"""
    ses_dict = read_yaml("conf.yaml")["SES"]
    session = Session(profile_name=ses_dict["PROFILE"])
    client = session.client("ses", region_name=ses_dict["AWS_REGION"])
    body_text = read_template(ses_dict["TEMPLATE"], **{"name": "Taku Ikegami"})
    try:
        response = client.send_email(
            Destination={
                "ToAddresses": [
                    ses_dict["RECIPIENT"],
                ],
            },
            Message={
                "Body": {
                    "Text": {
                        "Charset": ses_dict["CHARSET"],
                        "Data": body_text,
                    },
                },
                "Subject": {
                    "Charset": ses_dict["CHARSET"],
                    "Data": ses_dict["SUBJECT"],
                },
            },
            Source=ses_dict["SENDER"],
        )
    except ClientError as error:
        print(error.response["Error"]["Message"])
    else:
        print("Email sent! Message ID:")
        print(response["MessageId"])


if __name__ == "__main__":

    send_mail()
