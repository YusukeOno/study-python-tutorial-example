# study-python-tutorial-example
Studying is fun for me. Python language.

## Setup

### Initial

pip3コマンドを最新バージョンにする。

```
pip3 install --upgrade pip
```

Djangoをインストールする。

```
pip3 install Django
```

インストールが完了したら、以下のコマンドでDjangoのバージョンを確認する。

```
django-admin --version
```

### Create Project

初期プロジェクトの作成

Note: 使えない記号がある。ex. "-"

```
django-admin startproject [任意のプロジェクト名]
```

### Sratup Project

```
cd [任意のプロジェクト名]
python3 manage.py runserver
```

ブラウザから以下のURLにアクセスする。

```
http://127.0.0.1:8000/
```