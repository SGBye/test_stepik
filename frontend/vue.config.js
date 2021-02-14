module.exports = {
    "transpileDependencies": [
        "vuetify"
    ],
    devServer: {
        proxy: {
            '^/api/v1': {
                target: process.env.DEV_SERVER_PROXY_TARGET,
                ws: false
            }
        },
        port: 8080
    }
}