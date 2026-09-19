var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
const string VERSION = "v2"; const string BRANCH = "dotnet-v2";
app.MapGet("/", () => Results.Json(new { status = "ok", runtime = "dotnet", source = "github", version = VERSION, branch = BRANCH }));
app.MapGet("/health", () => Results.Json(new { status = "ok", runtime = "dotnet", source = "github", version = VERSION, branch = BRANCH }));
app.Run();
