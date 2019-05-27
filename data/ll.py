import yaml


def get_data_001():
    # [("123","123"),("hello","hello"),("#!!","#!!")]

    with open("./data_001.yml", "r", encoding="utf-8") as f:
        send_expect_data = []
        data = yaml.safe_load(f).get("TestSmsData")
        for i in data.values():
            send_expect_data.append((i.get("send"), i.get("expect")))
        return send_expect_data


a = get_data_001()
print(a)
