import runpod


def handler(job):
    """
    RunPod Serverless Entry Point
    """
    job_input = job.get("input", {})

    prompt = job_input.get("prompt", "")

    return {
        "status": "success",
        "message": "RunPod worker is running successfully.",
        "prompt_received": prompt
    }


runpod.serverless.start(
    {
        "handler": handler
    }
)