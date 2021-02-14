import urljoin from 'url-join';


const CLIENT_BASE_PATH = getClientBasePath();


function getClientBasePath() {
    return urljoin(window.location.origin, process.env.VUE_APP_CLIENT_PATH_POSTFIX);
}

export {CLIENT_BASE_PATH};
