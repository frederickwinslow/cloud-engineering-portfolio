output "resource_group_name" {
  description = "The name of the Azure resource group"
  value       = azurerm_resource_group.main.name
}

output "resource_group_location" {
  description = "The location of the Azure resource group"
  value       = azurerm_resource_group.main.location
}