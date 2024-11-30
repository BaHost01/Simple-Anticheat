-- Anti-Cheat Script for Roblox Studio

-- List of known cheats and exploit tools
local knownCheats = {
    "Synapse X", "Krnl", "JJSploit", "Proxo", "Sentinel", "Fluxus",
    "speedhack", "autoaim", "modded DLL", "external scripts"
}

-- Logging function
local function logActivity(message)
    local logMessage = string.format("[%s] %s", os.date("%Y-%m-%d %H:%M:%S"), message)
    print(logMessage)

    -- Example: Store logs in a ServerStorage log file (optional)
    local logsFolder = game:GetService("ServerStorage"):FindFirstChild("Logs") or Instance.new("Folder")
    logsFolder.Name = "Logs"
    logsFolder.Parent = game:GetService("ServerStorage")

    local logFile = logsFolder:FindFirstChild("AnticheatLogs") or Instance.new("StringValue")
    logFile.Name = "AnticheatLogs"
    logFile.Parent = logsFolder

    logFile.Value = logFile.Value .. "\n" .. logMessage
end

-- Function to report suspicious activity
local function reportCheater(player, reason)
    logActivity("Reporting player: " .. player.Name .. " for " .. reason)
    -- Add logic to ban or kick the player
    player:Kick("Suspicious activity detected: " .. reason)
end

-- Function to monitor player properties
local function monitorPlayer(player)
    local humanoid = player.Character:FindFirstChildOfClass("Humanoid")
    if not humanoid then return end

    -- Monitor WalkSpeed, JumpPower, and other properties
    local allowedWalkSpeed = 16
    local allowedJumpPower = 50

    while player.Parent do
        -- Check WalkSpeed
        if humanoid.WalkSpeed > allowedWalkSpeed then
            reportCheater(player, "Abnormal WalkSpeed (" .. humanoid.WalkSpeed .. ")")
            break
        end

        -- Check JumpPower
        if humanoid.JumpPower > allowedJumpPower then
            reportCheater(player, "Abnormal JumpPower (" .. humanoid.JumpPower .. ")")
            break
        end

        -- Delay for performance
        wait(1)
    end
end

-- Function to check player scripts for known exploits
local function monitorPlayerScripts(player)
    local suspiciousScripts = {"Synapse", "Krnl", "Exploit"}
    local playerScripts = player:FindFirstChildOfClass("PlayerScripts")

    if playerScripts then
        for _, scriptName in ipairs(suspiciousScripts) do
            if playerScripts:FindFirstChild(scriptName) then
                reportCheater(player, "Detected suspicious script: " .. scriptName)
            end
        end
    end
end

-- Monitor new players
game.Players.PlayerAdded:Connect(function(player)
    logActivity("Monitoring player: " .. player.Name)

    -- Wait for the player's character to load
    player.CharacterAdded:Connect(function(character)
        monitorPlayer(player)
        monitorPlayerScripts(player)
    end)

    -- Check existing character (in case it's already loaded)
    if player.Character then
        monitorPlayer(player)
        monitorPlayerScripts(player)
    end
end)

-- Monitor existing players (if the script is added after some players have joined)
for _, player in pairs(game.Players:GetPlayers()) do
    logActivity("Monitoring existing player: " .. player.Name)
    if player.Character then
        monitorPlayer(player)
        monitorPlayerScripts(player)
    end
    player.CharacterAdded:Connect(function()
        monitorPlayer(player)
        monitorPlayerScripts(player)
    end)
end

logActivity("Anti-Cheat initialized successfully.")
