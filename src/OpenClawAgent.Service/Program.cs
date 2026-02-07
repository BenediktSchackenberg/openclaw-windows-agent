using OpenClawAgent.Service;

var builder = Host.CreateApplicationBuilder(args);

// Add Windows Service support
builder.Services.AddWindowsService(options =>
{
    options.ServiceName = "OpenClaw Node Agent";
});

// Add configuration
builder.Services.AddSingleton(ServiceConfig.Load());

// Add our workers
builder.Services.AddHostedService<NodeWorker>();
builder.Services.AddHostedService<InventoryScheduler>();

var host = builder.Build();
host.Run();
