if __name__ == "__main__":
    def repeat(n):
        def deco(func):
            def wrapper():
                results = []
                for i in range(1, n + 1):
                    print(f"Вызов №{i} из {n}")
                    results.append(func())
                return results

            return wrapper

        return deco


    @repeat(9)
    def hi():
        return "Привет"


    print(hi())