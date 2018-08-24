from dataLoading.asyncRequestExecutor import asyncRequestExecutor
import asyncio
import aiohttp
import machineLearning.model as model
from dataLoading.parameterController import get_url_generator

async def asyncFetchAllData(identifier: dict):
    tasks = []
    async with aiohttp.ClientSession() as client:
        executor = asyncRequestExecutor(client)
        for url, params in get_url_generator(identifier):
            asyncLoadTask = asyncLoad(url, params, executor)
            tasks.append(asyncLoadTask)
        return await asyncio.gather(*tasks)

async def asyncLoad(url, paramDict, executor):
    matrix = await executor.getMatrixFromProtectedUrl(url)
    scores = model.get_network_score(matrix).tolist()
    return _format_matrix_result(paramDict, matrix, scores) 

# def append_model_estimation_scores(result: dict) -> dict:
#     matrix = result.get("matrix")
#     result["scores"] = model.getScoreForMatrix(matrix).tolist()
#     return result

def _format_matrix_result(params, matrix, scores=[]):
    return {
        "params": params,
        "matrix": matrix,
        "scores": scores
    }