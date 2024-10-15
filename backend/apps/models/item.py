from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime, timezone
from .group import Group
from .category import Category
from .image import Image


class Item(SQLModel, table=True):
    """
    備品（アイテム）情報を管理するモデル
    - `name`: アイテム名
    - `description`: アイテムの説明
    - `location`: アイテムの保管場所
    - `quantity`: 在庫数
    - `group_id`: 所属するグループID
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, description="アイテム名")
    description: Optional[str] = Field(max_length=255, description="アイテムの説明")
    location: str = Field(max_length=100, description="アイテムの保管場所")
    quantity: int = Field(description="在庫数")
    group_id: int = Field(foreign_key="group.id", description="グループID")

    # カテゴリとのリレーション
    category_id: int = Field(foreign_key="category.id", description="カテゴリID")
    category: Optional[Category] = Relationship(back_populates="items")

    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="作成日時"
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="更新日時"
    )

    # アイテムが属するグループ
    group: Optional[Group] = Relationship(back_populates="items")

    # アイテムに関連付けられた画像
    images: List[Image] = Relationship(back_populates="item")
