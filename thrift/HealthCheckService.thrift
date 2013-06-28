namespace py healthservice

exception ServiceError {
    1: string message
}

service HealthCheckService {
    void healthCheck() throws (1: ServiceError err)
}
