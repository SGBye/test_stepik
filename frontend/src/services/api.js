import axios from 'axios';
import { CLIENT_BASE_PATH} from '@/utils/constants';


const apiClient = axios.create({
    baseURL: CLIENT_BASE_PATH
});


class StepikAPI {
    constructor(apiClient) {
        this.apiClient = apiClient;
    }

    async ping() {
        return this.apiClient.get('ping/').then((response) => (response.data))
    }

    async checkCode(code) {
        return this.apiClient.post('solutions/', code).then((response) => (response.data))
    }

    async retrieveLastSolution() {
        return this.apiClient.get('last_user_solution/').then((response) => (response.data))
    }

    async checkSolutionStatus(id) {
        return this.apiClient.get(`check_solution_status/${id}/`).then((response) => (response.data))
    }
}

const stepikApi = new StepikAPI(apiClient);


export { stepikApi };
