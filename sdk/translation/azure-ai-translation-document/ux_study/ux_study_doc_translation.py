"""
1.	Translate the documents in your source container to french.
How many documents successfully translated and how many failed? (print the location of each translated document)
"""


def ux_task_1():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.translation.document import DocumentTranslationClient

    endpoint = "endpoint"
    key = "key"
    source_container_url = "source_container_url"
    target_container_url = "target_container_url_1"

    client = DocumentTranslationClient(endpoint, AzureKeyCredential(key))

    # write code here



if __name__ == '__main__':
    ux_task_1()
