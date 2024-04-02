class Solution {
    
    vector<int> BestIndex(vector<vector<int>>& points) {
        int n = points.size();
        
        vector<pair<int, int>> sum, dif;
        for (int j = 0; j < n; j ++) {
            sum.push_back({points[j][0] + points[j][1], j});
            dif.push_back({points[j][0] - points[j][1], j});
        }
        // We just need largest/smallest. 
        // Hencce, it can be done in O(N) as well instead of sorting.
        sort (sum.begin(), sum.end());
        sort (dif.begin(), dif.end());
        
        vector<int> result(n);
        for (int i = 0; i < n; i ++) {
            int cur_sum = points[i][0] + points[i][1];
            int cur_dif = points[i][0] - points[i][1];
            
            vector<pair<int, int>> all_4_cases = {
                // (Xi + Yi) - (Xj + Yj)
                {cur_sum - sum[0].first, sum[0].second},
                // (Xi - Yi) - (Xj - Yj)
                {cur_dif - dif[0].first, dif[0].second},
                // - (Xi - Yi) + (Xj - Yj)
                {-cur_dif + dif[n-1].first, dif[n-1].second},
                // - (Xi + Yi) + (Xj + Yj)
                {-cur_sum + sum[n-1].first, sum[n-1].second},
            };
            sort (all_4_cases.begin(), all_4_cases.end());
            
            result[i] = all_4_cases[3].second;
        }
        return result;
    }
    
    int Dist (const vector<vector<int>>& points, int i, int j) {
        return (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]));
    }
    
    vector<vector<int>> Remove (const vector<vector<int>>& points, int ind) {
        vector<vector<int>> result;
        
        for (int j = 0; j < points.size(); j ++) {
            if (j == ind) continue;
            result.push_back(points[j]);
        }
        return result;
    }
    
    int MaxDistanceIndex (const vector<vector<int>>& points, const vector<int>& best_ind) {
        int max_dist_ind = 0;
        int n = points.size();
        
        for (int i = 0; i < n; i ++) {
            if (Dist(points, i, best_ind[i]) > Dist(points, max_dist_ind, best_ind[max_dist_ind])) 
                max_dist_ind = i;
        }
        return max_dist_ind;
    }
    
public:
    int minimumDistance(vector<vector<int>>& points) {
        int n = points.size();
        
        vector<int> best_ind = BestIndex(points);
        int max_dist_ind = MaxDistanceIndex(points, best_ind);
        
        vector<vector<int>> points_except_i = Remove(points, max_dist_ind);
        vector<vector<int>> points_except_j = Remove(points, best_ind[max_dist_ind]);
        
        vector<int> best_ind_except_i = BestIndex(points_except_i);
        int max_dist_ind_except_i = MaxDistanceIndex(points_except_i, best_ind_except_i);
        
        vector<int> best_ind_except_j = BestIndex(points_except_j);
        int max_dist_ind_except_j = MaxDistanceIndex(points_except_j, best_ind_except_j);
        
        return min (
            Dist(points_except_i, max_dist_ind_except_i, best_ind_except_i[max_dist_ind_except_i]),
            Dist(points_except_j, max_dist_ind_except_j, best_ind_except_j[max_dist_ind_except_j])
        );
    }
};