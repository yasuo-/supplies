#!/bin/bash

# Monorepoのバックエンド内のSQLiteデータベースを使用して ER 図を生成
eralchemy -i sqlite:///backend/test.db -o ./docs/erd.png
