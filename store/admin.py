from django.contrib import admin
from .models import Category, FoodItem, Cart, Order, OrderItem

# Customizing the way FoodItem is displayed in the admin panel
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'category__name')
    list_editable = ('price', 'is_available')
    ordering = ('category', 'name')

# Making OrderItems show up directly within the Order view for easy reference
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('food_item', 'quantity', 'price')
    can_delete = False
    extra = 0 # Prevents showing extra empty forms

# Customizing the Order display
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'shipping_address')
    readonly_fields = ('user', 'total_price', 'shipping_address', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        # Disable the ability to manually add new orders from the admin panel
        return False

# Registering models with the admin site
admin.site.register(Category)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)

