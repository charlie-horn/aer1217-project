import numpy as np


class Cluster():
    def __init__(self):
        self.clusters = []
        self.threshold = 0.3
        self.minPts = 10
        return

    def cluster(self, locations, minPts):
        self.minPts = minPts
        print("Start Clustering")
        for i in range(len(locations)):
            location = locations[i]
            found = False

            for j in range(len(self.clusters)):
                cluster = self.clusters[j]['cluster']
                center = self.clusters[j]['center']
                dist = self.calc_dist(location, center)
                if dist < self.threshold:
                    cluster.append(location)
                    center = self.calc_center(cluster)
                    self.clusters[j] = {'center': center, 'cluster': cluster}
                    found = True
                    break
            if not found:
                self.clusters.append({'center': location, 'cluster': [location]})

        final_clusters = self.find_cluster(self.clusters, self.minPts)
        print('\nFinal Estimation:')
        for i in range(len(final_clusters)):
            print (final_clusters[i]['center'],len(final_clusters[i]['cluster']))

        return final_clusters

    def calc_dist(self, p1, p2):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        return np.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

    def calc_center(self, cluster):
        return np.mean(np.array(cluster), axis=0)

    def find_cluster(self, clusters, threshold):
        new_clusters = []
        for i in range(len(clusters)):
            cluster = clusters[i]['cluster']
            center = clusters[i]['center']
            if len(cluster) > threshold:
                new_clusters.append({'center': center, 'cluster': cluster})
        return new_clusters

