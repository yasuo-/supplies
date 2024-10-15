from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime, timezone
from .item import Item
from .user import User


class Image(SQLModel, table=True):
    """
    画像情報を管理するモデル
    - `url`: 画像の保存場所やURL
    - `item_id`: アイテムに関連する画像の場合のアイテムID
    - `user_id`: ユーザーに関連する画像の場合のユーザーID
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    url: str = Field(max_length=255, description="画像の保存場所やURL")
    item_id: Optional[int] = Field(
        foreign_key="item.id",
        description="アイテムID",
        default=None
    )
    user_id: Optional[int] = Field(
        foreign_key="user.id",
        description="ユーザーID",
        default=None
    )
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="作成日時"
    )

    # アイテムとのリレーション
    item: Optional[Item] = Relationship(back_populates="images")

    # ユーザーとのリレーション
    user: Optional[User] = Relationship(back_populates="images")
