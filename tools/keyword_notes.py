from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    """代表一个关键词及其关联的笔记条目"""
    keyword: str
    note: str
    source_url: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def summary(self) -> str:
        return f"[{self.keyword}] {self.note[:50]}..."


class NotesCollection:
    """管理一组 KeywordNote 对象的集合，并提供格式化输出"""

    def __init__(self, notes: Optional[List[KeywordNote]] = None):
        self.notes: List[KeywordNote] = notes if notes else []

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def filter_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if keyword.lower() in n.keyword.lower()]

    def all_keywords(self) -> List[str]:
        return list({n.keyword for n in self.notes})

    def format_as_simple_list(self) -> str:
        """简单列表格式"""
        lines = ["===== 关键词笔记列表 ====="]
        for i, note in enumerate(self.notes, 1):
            lines.append(f"{i}. {note.keyword} - {note.note}")
        return "\n".join(lines)

    def format_as_detailed_report(self) -> str:
        """详细报告格式"""
        lines = ["关键词笔记详细报告"]
        lines.append("=" * 30)
        for note in self.notes:
            lines.append(f"关键词: {note.keyword}")
            lines.append(f"笔记:   {note.note}")
            if note.source_url:
                lines.append(f"来源:   {note.source_url}")
            if note.tags:
                lines.append(f"标签:   {', '.join(note.tags)}")
            lines.append(f"创建时间: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            lines.append("-" * 30)
        return "\n".join(lines)

    def format_as_markdown_table(self) -> str:
        """Markdown 表格格式"""
        header = "| 序号 | 关键词 | 笔记 | 来源 | 标签 |"
        sep = "|------|--------|------|------|------|"
        rows = []
        for i, note in enumerate(self.notes, 1):
            url = note.source_url or ""
            tags = ", ".join(note.tags) if note.tags else ""
            rows.append(f"| {i} | {note.keyword} | {note.note} | {url} | {tags} |")
        return "\n".join([header, sep] + rows)


def create_sample_collection() -> NotesCollection:
    """创建包含示例数据的集合"""
    collection = NotesCollection()

    collection.add_note(KeywordNote(
        keyword="乐鱼体育",
        note="一个综合体育资讯平台，涵盖多种运动项目。",
        source_url="https://portal-m-leyusports.com.cn",
        tags=["体育", "资讯"]
    ))

    collection.add_note(KeywordNote(
        keyword="运动健身",
        note="定期锻炼有助于保持健康，建议每周至少运动3次。",
        tags=["健康", "生活方式"]
    ))

    collection.add_note(KeywordNote(
        keyword="赛事直播",
        note="热门体育赛事实时直播，用户可在线观看。",
        source_url="https://portal-m-leyusports.com.cn/live",
        tags=["直播", "体育"]
    ))

    collection.add_note(KeywordNote(
        keyword="营养饮食",
        note="均衡营养对运动表现和恢复至关重要。",
        tags=["饮食", "运动科学"]
    ))

    collection.add_note(KeywordNote(
        keyword="运动装备",
        note="选择合适运动装备可提升训练效果，减少受伤风险。",
        tags=["装备", "运动"]
    ))

    return collection


def format_collection(collection: NotesCollection, fmt: str = "simple") -> str:
    """根据 fmt 参数选择格式化方式： simple, detailed, table"""
    if fmt == "detailed":
        return collection.format_as_detailed_report()
    elif fmt == "table":
        return collection.format_as_markdown_table()
    else:
        return collection.format_as_simple_list()


if __name__ == "__main__":
    sample = create_sample_collection()
    print(format_collection(sample, "simple"))
    print("\n")
    print(format_collection(sample, "detailed"))
    print("\n")
    print(format_collection(sample, "table"))