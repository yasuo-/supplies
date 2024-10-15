from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime, timezone
from .item import Item
from .user import User


class Transaction(SQLModel, table=True):
    """
    備品の貸出・返却履歴を管理するモデル
    - `item_id`: アイテムID
    - `user_id`: ユーザーID
    - `transaction_type`: 取引の種類（貸出、返却）
    - `quantity`: 取引に関連する数量
    - `transaction_date`: 取引日
    """

    id: Optional[int] = Field(default=None, primary_key=True, description="自動インクリメントされるID")
    item_id: int = Field(foreign_key="item.id", description="アイテムID")
    user_id: int = Field(foreign_key="user.id", description="ユーザーID")
    transaction_type: str = Field(max_length=50, description="取引の種類（貸出 or 返却）")
    quantity: int = Field(description="数量")
    transaction_date: datetime = Field(description="取引日")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="作成日時"
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="更新日時"
    )

    # 取引されたアイテム
    item: Optional[Item] = Relationship()

    # 取引を行ったユーザー
    user: Optional[User] = Relationship()
