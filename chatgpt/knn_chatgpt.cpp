#include <bits/stdc++.h>

using namespace std;

// define a struct for each data point
struct DataPoint
{
    vector<double> features;
    int label;
};

// function to calculate euclidean distance between two data points
double euclideanDistance(DataPoint point1, DataPoint point2)
{
    double distance = 0;
    for (int i = 0; i < point1.features.size(); i++) {
    distance += pow(point1.features[i] - point2.features[i], 2);
    }
    return sqrt(distance);
}

// function to get the k nearest neighbors of a given data point
vector<DataPoint> getNeighbors(vector<DataPoint> dataset, DataPoint point, int k)
{
    vector<pair<double, int>> distances;
    for (int i = 0; i < dataset.size(); i++) {
    double distance = euclideanDistance(point, dataset[i]);
    distances.push_back({distance, i});
    }
// sort the distances in ascending order
    sort(distances.begin(), distances.end());

    vector<DataPoint> neighbors;

    for (int i = 0; i < k; i++) {
    neighbors.push_back(dataset[distances[i].second]);
    }
    return neighbors;
}

// function to get the most frequent label among the k nearest neighbors
int getLabel(vector<DataPoint> neighbors)
{
    unordered_map<int, int> labels;
    int maxCount = 0;
    int maxLabel = -1;
    for (int i = 0; i < neighbors.size(); i++)
    {
    labels[neighbors[i].label]++;
    if (labels[neighbors[i].label] > maxCount)
    {
        maxCount = labels[neighbors[i].label];
        maxLabel = neighbors[i].label;
    }
    }
    return maxLabel;
}

// main function to implement the knn algorithm
int knn(vector<DataPoint> trainSet, DataPoint testPoint, int k) {
vector<DataPoint> neighbors = getNeighbors(trainSet, testPoint, k);
int label = getLabel(neighbors);
return label;
}

int main() {
// example data points
vector<DataPoint> trainSet = {
{{1, 2, 3}, 1},
{{2, 3, 4}, 2},
{{3, 4, 5}, 2},
{{4, 5, 6}, 1},
{{5, 6, 7}, 3}
};
DataPoint testPoint = {{1.5, 2.5, 3.5}, 2};
int k = 3;
int label = knn(trainSet, testPoint, k);
cout << "Predicted label: " << label << endl;
return 0;
}