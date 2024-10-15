from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime, timezone
from .user import User
from .group import Group


class GroupUser(SQLModel, table=True):
    """
    グループとユーザーの中間テーブル
    - `group_id`: グループID
    - `user_id`: ユーザーID
    - `role`: グループ内でのユーザーの役割
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    group_id: int = Field(foreign_key="group.id", description="グループID")
    user_id: int = Field(foreign_key="user.id", description="ユーザーID")
    role: str = Field(max_length=50, description="グループ内でのユーザーの役割")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="作成日時"
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="更新日時"
    )

    # ユーザーとのリレーション
    user: Optional[User] = Relationship(back_populates="groups")

    # グループとのリレーション
    group: Optional[Group] = Relationship(back_populates="users")
