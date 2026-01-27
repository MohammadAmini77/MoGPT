

from llama_index.llms.ollama import Ollama   # Ollama LLM wrapper
from config.settings import Settings
settings = Settings()                        # Load configuration
OLLAMA_URL = settings.OLLAMA_URL             # Ollama server URL

# Cache current model and LLM instance
_current_model_name = None
_current_llm_instance = None


def get_ollama_llm(model_name: str):
    global _current_model_name, _current_llm_instance  # Use module-level cache

    # Return cached instance if model is already loaded
    if _current_model_name == model_name and _current_llm_instance is not None:
        return _current_llm_instance

    # Create new Ollama LLM instance
    llm = Ollama(base_url=OLLAMA_URL, model=model_name)

    # Update cache
    _current_model_name = model_name
    _current_llm_instance = llm

    return llm  # Return LLM instance




#Example usage
check_llm = get_ollama_llm(model_name="llama3:latest")
print(check_llm)
print(type(check_llm))