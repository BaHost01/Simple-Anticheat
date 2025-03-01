-- Advanced Roblox Anticheat Admin GUI (Client Side)
-- Place this LocalScript inside StarterGui for admin monitoring.

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")
local cheatAlertEvent = ReplicatedStorage:WaitForChild("CheatAlertEvent")
local localPlayer = Players.LocalPlayer

-- Create a ScreenGui for the admin interface.
local adminGui = Instance.new("ScreenGui")
adminGui.Name = "AnticheatAdminGui"
adminGui.ResetOnSpawn = false
adminGui.Parent = localPlayer:WaitForChild("PlayerGui")

-- Main container frame.
local mainFrame = Instance.new("Frame")
mainFrame.Size = UDim2.new(0, 500, 0, 350)
mainFrame.Position = UDim2.new(0, 20, 0, 20)
mainFrame.BackgroundColor3 = Color3.fromRGB(25, 25, 25)
mainFrame.BackgroundTransparency = 0.1
mainFrame.Parent = adminGui

-- Title label.
local titleLabel = Instance.new("TextLabel")
titleLabel.Size = UDim2.new(1, -10, 0, 40)
titleLabel.Position = UDim2.new(0, 5, 0, 5)
titleLabel.BackgroundTransparency = 1
titleLabel.Text = "Anticheat Admin Alerts"
titleLabel.TextColor3 = Color3.new(1, 1, 1)
titleLabel.Font = Enum.Font.SourceSansBold
titleLabel.TextSize = 24
titleLabel.Parent = mainFrame

-- Scrolling frame for alerts.
local alertFrame = Instance.new("ScrollingFrame")
alertFrame.Size = UDim2.new(1, -10, 1, -60)
alertFrame.Position = UDim2.new(0, 5, 0, 50)
alertFrame.BackgroundColor3 = Color3.fromRGB(20, 20, 20)
alertFrame.BackgroundTransparency = 0.3
alertFrame.ScrollBarThickness = 8
alertFrame.Parent = mainFrame

local uiListLayout = Instance.new("UIListLayout")
uiListLayout.SortOrder = Enum.SortOrder.LayoutOrder
uiListLayout.Parent = alertFrame

-- Function to add a new alert label.
local function addAlert(message)
    local alertLabel = Instance.new("TextLabel")
    alertLabel.Size = UDim2.new(1, 0, 0, 30)
    alertLabel.BackgroundTransparency = 1
    alertLabel.Text = message
    alertLabel.TextColor3 = Color3.fromRGB(255, 100, 100)
    alertLabel.Font = Enum.Font.SourceSans
    alertLabel.TextSize = 18
    alertLabel.Parent = alertFrame
    -- Automatically scroll to the bottom.
    wait(0.1)
    alertFrame.CanvasPosition = Vector2.new(0, uiListLayout.AbsoluteContentSize.Y)
end

-- Listen for cheat alerts from the server.
cheatAlertEvent.OnClientEvent:Connect(function(message)
    addAlert(message)
end)
