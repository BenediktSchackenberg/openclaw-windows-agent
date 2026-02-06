namespace OpenClawAgent.Models;

/// <summary>
/// Log entry for display in dashboard and logs view
/// </summary>
public class LogEntry
{
    public DateTime Timestamp { get; set; }
    public string Level { get; set; } = "info";
    public string Source { get; set; } = "";
    public string Message { get; set; } = "";
    
    public string TimeString => Timestamp.ToString("HH:mm:ss");
    
    public string LevelEmoji => Level switch
    {
        "success" => "✅",
        "error" => "❌",
        "warning" => "⚠️",
        "event" => "📨",
        "debug" => "🔧",
        _ => "ℹ️"
    };
}
