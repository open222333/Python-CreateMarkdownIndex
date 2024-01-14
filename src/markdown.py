

class Markdown():

    def __init__(self) -> None:
        pass

    def generate_markdown_table(self, headers, data):
        """Generate a Markdown table.

        Args:
            headers (list): List of strings representing table headers.
            data (list of lists): List of lists representing table rows.

        Returns:
            str: Markdown representation of the table.
        """
        header_row = f"| {' | '.join(headers)} |"
        separator_row = f"| {' | '.join(['---'] * len(headers))} |"
        data_rows = "\n".join(f"| {' | '.join(map(str, row))} |" for row in data)
        markdown_table = f"{header_row}\n{separator_row}\n{data_rows}"
        return markdown_table


class MarkdownIndexGenerator():

    def __init__(self, target_path: str = 'index.md') -> None:
        self.target_path = target_path


if __name__ == "__main__":
    # 創建表格範例
    headers = ["Name", "Age", "Occupation"]
    data = [
        ["Alice", 28, "Engineer"],
        ["Bob", 35, "Designer"],
        ["Charlie", 42, "Manager"]
    ]

    m = Markdown()
    markdown_table = m.generate_markdown_table(headers, data)
    print(markdown_table)
