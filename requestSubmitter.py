"""
Client to submit new render request to server
"""

import logging

from util import client


LOGGER = logging.getLogger(__name__)



def send(d):
    """
    Send/Submit a new render request

    :param d: dict. a render request serialized as dictionary
    """
    rrequest = client.add_request(d)
    if rrequest:
        LOGGER.info('request %s sent to server', rrequest.uid)



"""
    ######################
    #####   PARAMS   #####
    ######################

    :param uid: str. unique identifier, server as primary key for database
    :param name: str. job name
    :param owner: str. the name of the submitter
    :param worker: str. the name of the worker to render the job
    :param time_created: str. datetime in .strftime("%m/%d/%Y, %H:%M:%S") format
    :param priority: int. job priority [0 lowest to 100 highest]
    :param category: str.
    :param tags: [str].
    :param status: RenderStatus. job render status
    :param umap_path: str. Unreal path to the map/level asset
    :param useq_path: str. Unreal path to the sequence asset
    :param uconfig_path: str. Unreal path to the preset/config asset
    :param output_path: str. system path to the output directory
    :param width: int. output width
    :param height: int. output height
    :param frame_rate: int. output frame rate
    :param format: int. output format
    :param start_frame: int. custom render start frame
    :param end_frame: int. custom render end frame
    :param time_estimate: str. render time remaining estimate
    :param progress: int. render progress [0 to 100]
"""

if __name__ == '__main__':
    job1 = {
        'name': 'jobName',
        'owner': 'TEST_SUBMITTER_01',
        'umap_path': '/Game/Main.Main',
        'useq_path': '/Game/NewLevelSequence.NewLevelSequence',
        'uconfig_path': '/Game/tempConfig061123.tempConfig061123',
        'output_path': r'C:\Users\Bøgh\Documents\Projects\unrealRenderFarm\test_renders'
    }

    jobs = [job1]

    for job in jobs:
        send(job)
