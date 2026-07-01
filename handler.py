import runpod


def handler(job):
    """
    This function is called every time a request reaches the RunPod endpoint.
    """

    job_input = job["input"]

    prompt = job_input.get("prompt", "")

    return {
        "status": "success",
        "message": "RunPod worker is working!",
        "prompt": prompt
    }


runpod.serverless.start({"handler": handler})