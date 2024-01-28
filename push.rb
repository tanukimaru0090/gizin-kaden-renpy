message = ARGV[0]
branch = ARGV[1]

system('git add .')
system("git commit -m '#{message}'")
res = `git push origin #{branch}`
puts res
