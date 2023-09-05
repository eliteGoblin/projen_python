from typing import Any


def run_wiz(
    ghe_webhook_message: dict[str, Any],
) -> dict[str, Any]:
    """
    Run wizcli iac scan, per GHE webhook event

    Args:
        GHE_webhook_message (dict): GHE event body from webhook

    Returns:
        dict: payload for GHE checkrun API(or as part of final response)
    """
    # echo dict, will be replaced after CSWI-110 finish
    return ghe_webhook_message
