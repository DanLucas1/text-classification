from skllm.config import SKLLMConfig

key = input('enter openAI key:\n')
org = input('enter openAI organization ID: \n')

SKLLMConfig.set_openai_key(f'{key}')
SKLLMConfig.set_openai_org(f'{org}')
print('finished setup')
