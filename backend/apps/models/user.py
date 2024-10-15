from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime, timezone

from .group_user import GroupUser


class User(SQLModel, table=True):
    """
    ユーザー情報を管理するモデル
    - `username`: ユーザー名（ユニーク）
    - `email`: メールアドレス（ユニーク）
    - `hashed_password`: ハッシュ化されたパスワード
    - `is_active`: ユーザーがアクティブかどうか
    - `is_superuser`: ユーザーが管理者かどうか
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(max_length=50, unique=True, description="ユーザー名")
    email: str = Field(max_length=255, unique=True, description="メールアドレス")
    hashed_password: str = Field(max_length=255, description="パスワード")
    is_active: bool = Field(default=True, description="ユーザーがアクティブかどうか")
    is_superuser: bool = Field(default=False, description="管理者かどうか")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="作成日時"
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="更新日時"
    )

    # ユーザーが所属するグループとの関係（多対多）
    groups: List["GroupUser"] = Relationship(back_populates="user")
