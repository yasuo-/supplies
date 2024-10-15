from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime, timezone

from .group_user import GroupUser


class Group(SQLModel, table=True):
    """
    グループ情報を管理するモデル
    - `name`: グループ名（ユニーク）
    - `description`: グループの説明
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True, description="グループ名")
    description: Optional[str] = Field(max_length=255, description="グループの説明")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="作成日時"
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="更新日時"
    )
    # グループに所属するユーザーとの関係（多対多）
    users: List["GroupUser"] = Relationship(back_populates="group")
