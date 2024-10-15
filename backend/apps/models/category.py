from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime, timezone

from .item import Item


class Category(SQLModel, table=True):
    """
    カテゴリ情報を管理するモデル
    - `name`: カテゴリ名
    - `description`: カテゴリの説明
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True, description="カテゴリ名")
    description: Optional[str] = Field(max_length=255, description="カテゴリの説明")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="作成日時"
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="更新日時"
    )

    items: List["Item"] = Relationship(back_populates="category")
