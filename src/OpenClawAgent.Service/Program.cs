using OpenClawAgent.Service;

var builder = Host.CreateApplicationBuilder(args);

// Add Windows Service support
builder.Services.AddWindowsService(options =>
{
    options.ServiceName = "OpenClaw Node Agent";
});

// Add our worker
builder.Services.AddHostedService<NodeWorker>();

// Add configuration
builder.Services.AddSingleton<ServiceConfig>();

var host = builder.Build();
host.Run();
