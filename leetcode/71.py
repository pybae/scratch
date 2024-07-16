class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        for directory in path.split("/"):
            if directory == "" or directory == ".":
                continue
            elif directory == "..":
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(directory)
        return "/" + "/".join(stack[1:])

sol = Solution()
print(sol.simplifyPath("/home//asdf"))
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath("/.././"))
print(sol.simplifyPath("/.../a/../b/c/../d/./"))
