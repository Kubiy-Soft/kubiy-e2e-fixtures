# kubiy-e2e-fixtures

Fixtures para probar **deploys desde GitHub** en Kubiy. Un branch por runtime/versión;
cada branch tiene la app en la raíz y `/health` responde `{runtime, source:"github", version, branch}`.

Branches: `node`/`node-v2`, `python`/`python-v2`, `go`/`go-v2`, `dotnet`/`dotnet-v2`.
