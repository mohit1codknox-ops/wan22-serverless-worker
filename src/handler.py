import runpod


def handler(event):
    """
    RunPod Serverless handler.
    """
    job_input = event.get("input", {})

    prompt = job_input.get("prompt", "")

    return {
        "status": "success",
        "message": "RunPod worker is running successfully.",
        "prompt_received": prompt
    }


if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})