from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime, timezone
from .user import User


class AccessToken(SQLModel, table=True):
    """
    アクセストークンを管理するモデル
    - `token`: アクセストークン
    - `user_id`: トークンが属するユーザーID
    - `expires_at`: トークンの有効期限
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    token: str = Field(max_length=255, unique=True, description="アクセストークン")
    user_id: int = Field(foreign_key="user.id", description="ユーザーID")
    expires_at: Optional[datetime] = Field(description="トークンの有効期限")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="作成日時"
    )

    user: Optional[User] = Relationship(back_populates="access_tokens")
