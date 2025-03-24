from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Don't you just want to dupe email?,
        well instead of name, just do account

        yeah you have to dfs it, ehhh, rushed into the solution eh,
        thinking about three nodes help. okay so how to dfs
        """

        account_to_emails: dict[int, list[str]] = {}
        email_to_accounts: dict[str, set[int]] = {}

        for i, account in enumerate(accounts):
            account_to_emails[i] = account[1:]
            for email in account[1:]:
                if email not in email_to_accounts:
                    email_to_accounts[email] = []
                email_to_accounts[email].append(i)

        result = []
        for i in range(len(accounts)):
            if i in account_to_emails:
                indices = self.dfs(i, [], account_to_emails, email_to_accounts)
                result.append(
                    [accounts[indices[0]][0]] + 
                    sorted(list(set(email for index in indices for email in accounts[index][1:])))
                )

        return result

    def dfs(self, account: int, result: List[str],
            account_to_emails: dict[int, list[str]], 
            email_to_accounts: dict[str, set[int]]) -> List[str]:

        result.append(account)
        emails = account_to_emails.pop(account)
        for email in emails:
            if account in email_to_accounts[email]:
                email_to_accounts[email].remove(account)

        for email in emails:
            if email in email_to_accounts:
                for connected_account in email_to_accounts[email]:
                    self.dfs(connected_account, result, account_to_emails, email_to_accounts)

        return result
        



sol = Solution()
print(sol.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
print(sol.accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))
