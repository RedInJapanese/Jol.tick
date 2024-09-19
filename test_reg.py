from lupa import LuaRuntime

# Create a Lua runtime
lua = LuaRuntime(unpack_returned_tuples=True)

# Load and run the Lua file
with open("example.lua", "r") as lua_file:
    lua_code = lua_file.read()

lua.execute(lua_code)

# Access Lua variables and functions from Python
lua_variable = lua.globals().variable_from_lua
lua_function = lua.globals().greet()

print(f"Variable from Lua: {lua_variable}")
print(f"Greeting from Lua: {lua_function}")
