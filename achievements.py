class Achievements:
    def __init__(self):
        self.unlocked = set()

    def check(self, lines, score, bonuses_used):
        new_achievements = []
        
        goals = [
            ("FIRST LINE", lines >= 1),
            ("BUS MASTER", lines >= 10),
            ("1000 POINTS", score >= 1000),
            ("TICKET CHECK", bonuses_used >= 1),
            ("INSPECTOR PRO", bonuses_used >= 5)
        ]
        
        for name, completed in goals:
            if completed and name not in self.unlocked:
                self.unlocked.add(name)
                new_achievements.append(name)
                
        return new_achievements