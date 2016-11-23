# -*- coding: utf-8 -*-

from intelmq.lib import utils
from intelmq.lib.bot import Bot


class Malc0deDomainBlacklistParserBot(Bot):

    def process(self):
        report = self.receive_message()

        raw_report = utils.base64_decode(report.get("raw"))

        for row in raw_report.splitlines():

            row = row.strip()
            if row == "" or row[:2] == "//":
                continue

            event = self.new_event(report)

            event.add('classification.type', 'malware')
            event.add('source.fqdn', row.split(" ")[1])
            event.add('raw', row)

            self.send_message(event)
        self.acknowledge_message()
