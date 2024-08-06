from datetime import datetime

import numpy as np

from routers.algorithms.queries.clustering_query import plot_dendrogram, single_linkage_clustering
from routers.algorithms.schemas.algorithms_schema import ClusteringBody, ClusteringResponse


class SingleLinkageClusteringController:
    def __init__(self, body: ClusteringBody) -> None:
        self.distance_matrix = np.array(body.distance_matrix)
        self.filename = body.filename

    def run(self):
        start_time = datetime.now()
        clusters, history = single_linkage_clustering(self.distance_matrix.copy())
        end_time = datetime.now()

        execution_time = (end_time - start_time).total_seconds()
        plot_dendrogram(history, "Agrupamiento por Enlace Simple", f"{self.filename}_single_linkage.png")

        response = ClusteringResponse(
            execution_time=execution_time,
            clusters=clusters,
            history=history
        )
        return response