from openai import OpenAI
from load_gdrant import global_config
llm_client = OpenAI(
    api_key=global_config.get(
        "NVIDIA_API_KEY"
    ),
    base_url=global_config.get(
        "NVIDIA_BASE_URL",
        "https://integrate.api.nvidia.com/v1"
    )
)


llm_tool_client = OpenAI(
    api_key=global_config.get(
        "OPENROUTER_API_KEY"
    ),
    base_url=global_config.get(
        "OPENROUTER_BASE_URL",
        "https://openrouter.ai/api/v1"
    )
)
