from urllib.parse import urlparse, urlencode, urlunparse, parse_qs

from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def build_next_offset_url(url: str, param_name: str, step: int) -> str:
    """
    Builds a new URL by incrementing a numeric query parameter (offset-based pagination).

    Args:
        url (str): The original URL containing query parameters.
        param_name (str): The name of the query parameter to increment (e.g. "jobOffset").
        step (int): The amount to add to the current parameter value.

    Returns:
        str: A new URL with the updated query parameter value.
    """
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    current_value = int(query_params.get(param_name, [0])[0])
    query_params[param_name] = [str(current_value + step)]

    new_query = urlencode(query_params, doseq=True)

    return urlunparse(parsed._replace(query=new_query))

def get_key_value(response):
    """
    Extracts key-value pairs from a Scrapy response object.

    This function is intended to parse structured fields from an HTML response
    (such as labels and values in job detail pages) and return them as a dictionary.

    Typical use cases include extracting metadata like:
    - Work Location
    - Employment Type
    - Department
    - Job ID

    Args:
        response (scrapy.http.Response): The Scrapy response object containing HTML content.

    Returns:
        dict: A dictionary where keys are field names and values are the extracted text.
    """

    data = {}

    fields = response.css(".article__content__view__field")

    for field in fields:
        label = field.css(
            ".article__content__view__field__label::text"
        ).get()

        value = field.css(
            ".article__content__view__field__value"
        )

        if not value:
            continue

        value_text = value.xpath("string(.)").get(default="").strip()

        if label:
            data[label.strip()] = value_text
        else:
            if ":" in value_text:
                key, val = value_text.split(":", 1)
                data[key.strip()] = val.strip()

    return data