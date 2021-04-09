import numpy as np


class Cluster():
    def __init__(self):
        self.clusters = []  # [{'center':center, 'cluster': [points]},...]
        self.threshold = 0.3  # distance threshold
        self.minPts = 5   # minimum number of points in cluster
        return

    def cluster(self, locations):
        print("Start Clustering")
        for i in range(len(locations)): # go through each point
            location = locations[i]
            found = False # flag

            for j in range(len(self.clusters)):  # go through each cluster
                cluster = self.clusters[j]['cluster']
                center = self.clusters[j]['center']
                dist = self.calc_dist(location, center)
                # if the distance is less than the threshold, the point belongs to the current cluster
                if dist < self.threshold:
                    cluster.append(location)
                    center = self.calc_center(cluster)  # update center
                    self.clusters[j] = {'center': center, 'cluster': cluster} # update cluster
                    found = True
                    break
            # create new cluster if the point does not belong to any clusters
            if not found:
                self.clusters.append({'center': location, 'cluster': [location]})
        
        # find good clusters that have at least minimum number of points 
        final_clusters = self.find_cluster(self.clusters, self.minPts)
        
        # print result
        print('\nFinal Estimation:')
        for i in range(len(final_clusters)):
            print (final_clusters[i]['center'])

        return final_clusters

    def calc_dist(self, p1, p2):
        # calculate the distance between the point and the cluster center
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        return np.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

    def calc_center(self, cluster):
        # find the center of the cluster
        return np.mean(np.array(cluster), axis=0)

    def find_cluster(self, clusters, threshold):
        # find good clusters 
        new_clusters = []
        for i in range(len(clusters)):
            cluster = clusters[i]['cluster']
            center = clusters[i]['center']
            if len(cluster) > threshold:
                new_clusters.append({'center': center, 'cluster': cluster})
        return new_clusters

