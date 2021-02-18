import axios from 'axios';
import {CLIENT_BASE_PATH} from '@/utils/constants';


const apiClient = axios.create({
    baseURL: CLIENT_BASE_PATH
});


apiClient.interceptors.response.use(function (response) {
    return response.data;
  }, function (error) {
    return Promise.reject(error.response);
  });


class StepikAPI {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async ping() {
        return this.apiClient.get('ping/')
    }

    async checkCode(code) {
        return this.apiClient.post('solutions/', code)
    }

    async retrieveLastSolution() {
        return this.apiClient.get('last_user_solution/')
    }

    async checkSolutionStatus(id) {
        return this.apiClient.get(`check_solution_status/${id}/`)
    }
}

const stepikApi = new StepikAPI(apiClient);


export {stepikApi};
